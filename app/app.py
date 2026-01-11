from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate

app = FastAPI()


text_post= {1 : {"title" : "New Post","content" : "cool test post"},
            2 : {"title2": "Second Post", "content2":"cool test post 2"},
            3 : {"title3": "Second3 Post", "content2":"cool test post 2"},
            4 : {"title4": "Second4 Post", "content2":"cool test post 2"},
            5 : {"title5": "Second5 Post", "content2":"cool test post 2"},
            6 : {"title6": "Second6 Post", "content2":"cool test post 2"},
            7 : {"title7": "Second7 Post", "content2":"cool test post 2"}}
@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return text_post[:limit]
    return text_post

@app.get("/posts/{id}")
def get_id_post(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not Found")

    return text_post.get(id)



