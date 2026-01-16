
# DataBridge

DataBridge connects MENA talent with AI data-labeling opportunities. The platform trains, certifies, and evaluates annotators, while providing AI startups with high-quality labeled datasets.

## Features

- Landing page collecting waitlist signups
- Supabase backend for storing users, CSVs, and files
- Hosted Python backend (FastAPI) for analyzing CSV labeling quality
- Generates accuracy scores, IAA metrics, and certification badges

## Tech Stack

- Frontend: Lovable → GitHub → Vercel
- Backend (user data / file storage): Supabase
- Python tool: FastAPI + pandas
- Hosting: Vercel (frontend) + Render.com / Railway (Python backend)

## Setup

1. Clone repo
2. If using locally: open frontend/index.html in a browser
3. Deploy frontend via Vercel
4. Deploy Python backend via Render/Railway
5. Connect backend to Supabase to read CSVs and store results
