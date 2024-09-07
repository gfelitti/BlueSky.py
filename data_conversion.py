import pandas as pd

def convert_profile_to_df(profile_data):
    profile_dict = {
        "did": profile_data['did'],
        "handle": profile_data['handle'],
        "display_name": profile_data.get('displayName'),
        "description": profile_data.get('description'),
        "followers_count": profile_data.get('followersCount'),
        "follows_count": profile_data.get('followsCount'),
        "posts_count": profile_data.get('postsCount'),
        "created_at": profile_data.get('createdAt'),
        "indexed_at": profile_data.get('indexedAt')
    }
    
    return pd.DataFrame([profile_dict])

def convert_posts_to_df(posts_data):
    posts_list = [{
        "uri": post['post']['uri'],
        "cid": post['post']['cid'],
        "text": post['post']['record']['text'],
        "created_at": post['post']['record']['createdAt'],
        "reply_count": post['post']['replyCount'],
        "repost_count": post['post']['repostCount'],
        "like_count": post['post']['likeCount'],
        "indexed_at": post['post']['indexedAt'],
        "author_handle": post['post']['author']['handle'],
        "author_display_name": post['post']['author']['displayName'],
        "author_did": post['post']['author']['did']
    } for post in posts_data]
    
    return pd.DataFrame(posts_list)

def convert_search_to_df(posts_data):
    posts_list = [{
        "uri": post['uri'],
        "cid": post['cid'],
        "text": post['record']['text'],
        "created_at": post['record']['createdAt'],
        "reply_count": post['replyCount'],
        "repost_count": post['repostCount'],
        "like_count": post['likeCount'],
        "indexed_at": post['indexedAt'],
        "author_handle": post['author']['handle'],
        "author_display_name": post['author']['displayName'],
        "author_did": post['author']['did']
    } for post in posts_data]
    
    return pd.DataFrame(posts_list)