import uuid

from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

from backend.api.v1.feed import FeedType

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


# TODO : response mode - для него нужен pydantic. Когда мы будем использщовать его
#  он автоматически будет присекать лишнее и отдаватьб только те параметры которые у него есть
#
class PostBrief(BaseModel):
    id: int
    title: str
    slug: str


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_post():
    return {"msg":"post created"}


# query параметры
@router.get(
    "/",
    status_code=status.HTTP_200_OK
)
async def list_posts(
        page: int = 1,
        size: int = 10,
        q: str | None = None,
        tags: str | None = None,
        feed: FeedType = FeedType.new
):
    return {
        "posts": [],
        "page": page,
        "size": size,
        "q": q,
        "tags": tags,
        "feed": feed
    }


@router.get("/popular")
async def get_popular_posts():
    return {"popular_posts": []}


@router.get(
    "{/post_id}",
    response_model=PostBrief,
)
async def get_post(post_id: int):
    return {
        "id": post_id,
        "title": f"Post {post_id}",
        "slug": f"Post {post_id}",
        "hashed_password": "secret",
        "internal_id": 12345
    }


@router.delete(
    "/{post_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_post(post_id: int):
    return None