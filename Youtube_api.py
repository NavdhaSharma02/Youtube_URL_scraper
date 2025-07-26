#youtube api script
#pip install google-api-python-client pandas openai-whisper langcodes
#pip install isodate

import pandas as pd
from googleapiclient.discovery import build
import isodate  

API_KEY = 'insert_Api_key'  
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_duration(video_id):
    """
    Get the duration of a video in seconds from video ID.
    """
    response = youtube.videos().list(
        part='contentDetails',
        id=video_id
    ).execute()

    if 'items' in response and len(response['items']) > 0:
        duration_iso = response['items'][0]['contentDetails']['duration']
        duration_sec = isodate.parse_duration(duration_iso).total_seconds()
        return duration_sec
    return 0

def get_videos_from_channel(channel_id):
    """
    Get all videos from channel (with pagination).
    """
    videos = []
    next_page_token = None
    while True:
        request = youtube.search().list(
            part='id,snippet',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            type='video',
            order='date'
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            url = f'https://www.youtube.com/watch?v={video_id}'

            # duration filter ≥ 3600 seconds (1 hour)
            duration = get_video_duration(video_id)
            if duration >= 3600:
                videos.append({
                    'video_id': video_id,
                    'title': title,
                    'url': url,
                    'duration_sec': duration
                })

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    return videos

channel_languages = {
    'insert_channel_id_here': 'insert_channel_podcast_language',
}

def main():
    all_videos = []
    for channel_id, lang_code in channel_languages.items():
        print(f"Fetching long videos for channel {channel_id}...")
        videos = get_videos_from_channel(channel_id)
        for video in videos:
            video['language'] = lang_code
            all_videos.append(video)

    df = pd.DataFrame(all_videos)
    df = df[['url', 'language']]
    df.to_csv('youtube_long_videos_with_languages.csv', index=False)
    print("CSV saved: youtube_long_videos_with_languages.csv")

if __name__ == "__main__":
    main()

