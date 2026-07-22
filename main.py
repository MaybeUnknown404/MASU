from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI(title="Anime Proxy API")

# Setup folder templates untuk UI
templates = Jinja2Templates(directory="templates")

# Base URL dari API asli
BASE_TARGET_URL = "https://animeku.my.id"

# Helper Headers
def get_headers():
    return {
        "User-Agent": "okhttp/3.12.13",
        "Data-Agent": "AnimeXNonton 2026.4.6/13",
        "Content-Type": "application/x-www-form-urlencoded"
    }

# --- ENDPOINT UI HALAMAN UTAMA ---
@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- ENDPOINT UI HALAMAN GENRE ---
@app.get("/genre", response_class=HTMLResponse)
async def serve_genre_page(request: Request):
    return templates.TemplateResponse("genre.html", {"request": request})

# --- ENDPOINT UI HALAMAN DETAIL ---
@app.get("/detail", response_class=HTMLResponse)
async def serve_detail_page(request: Request):
    return templates.TemplateResponse("detail.html", {"request": request})
    
# --- ENDPOINT UI HALAMAN JADWAL ---
@app.get("/schedule", response_class=HTMLResponse)
async def serve_schedule_page(request: Request):
    return templates.TemplateResponse("schedule.html", {"request": request})

# --- ENDPOINT UI HALAMAN PLAYER ---
@app.get("/player", response_class=HTMLResponse)
async def serve_player_page(request: Request):
    return templates.TemplateResponse("player.html", {"request": request})

# --- ENDPOINT UI HALAMAN PENCARIAN ---
@app.get("/search", response_class=HTMLResponse)
async def serve_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

# ---------------------------------------------------------
# 1. API: HOME (GET POSTS)
# ---------------------------------------------------------
@app.post("/nontonanime-x/phalcon/api/get_posts/")
async def proxy_get_posts(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/get_posts/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()

# ---------------------------------------------------------
# 2. API: SEMUA ANIME (CATEGORY NOT ONGOING)
# ---------------------------------------------------------
@app.post("/nontonanime-x/phalcon/api/get_category_not_ongoing/")
async def proxy_get_category_not_ongoing(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/get_category_not_ongoing/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()

# ---------------------------------------------------------
# 3. API: JADWAL (CATEGORY ONGOING)
# ---------------------------------------------------------
@app.post("/nontonanime-x/phalcon/api/get_category_ongoing/")
async def proxy_get_category_ongoing(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/get_category_ongoing/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()

# ---------------------------------------------------------
# 4. API: DAFTAR GENRE
# ---------------------------------------------------------
@app.get("/nontonanime-x/phalcon/api/get_anime_genre_list/")
async def proxy_get_anime_genre_list():
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/get_anime_genre_list/"
    headers = {"User-Agent": "okhttp/3.12.13", "Data-Agent": "AnimeXNonton 2026.4.6/13"}
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(target_url, headers=headers)
    return response.json()

# ---------------------------------------------------------
# 5. API: FILTER ANIME BERDASARKAN GENRE
# ---------------------------------------------------------
@app.post("/nontonanime-x/phalcon/api/get_anime_by_genre/")
async def proxy_get_anime_by_genre(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/get_anime_by_genre/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()

# ---------------------------------------------------------
# 6. API: DETAIL ANIME & DAFTAR EPISODE
# ---------------------------------------------------------
@app.post("/nontonanime-v77/phalcon/api/get_category_posts_secure/v9_1/")
async def proxy_get_category_posts_secure(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-v77/phalcon/api/get_category_posts_secure/v9_1/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()

# ---------------------------------------------------------
# 7. API: DESKRIPSI & LINK STREAMING VIDEO
# ---------------------------------------------------------
@app.post("/nontonanime-x/phalcon/api/get_post_description/")
async def proxy_get_post_description(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/get_post_description/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()
    
# ---------------------------------------------------------
# 8. API: PENCARIAN ANIME (SEARCH)
# ---------------------------------------------------------
@app.post("/nontonanime-x/phalcon/api/search_category_collection/")
async def proxy_search_anime(request: Request):
    form_data = dict(await request.form())
    target_url = f"{BASE_TARGET_URL}/nontonanime-x/phalcon/api/search_category_collection/"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.post(target_url, data=form_data, headers=get_headers())
    return response.json()