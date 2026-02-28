# ASCK Chatbot

A powerful Q&A knowledge base chatbot skeleton, built with a modern frontend and a robust Python backend.

## 🚀 Features

-   **Modern UI**: Built with [Ant Design X](https://x.ant.design/) and React, providing a premium chat experience.
-   **Robust Backend**: Powered by [FastAPI](https://fastapi.tiangolo.com/) for high performance and easy extension.
-   **RAG Ready**: Pre-configured for integration with [Weaviate](https://weaviate.io/) for Retrieval-Augmented Generation.
-   **Developer Friendly**: Monorepo structure with automated scripts for initialization and management.

## 🛠️ Tech Stack

-   **Frontend**: Vite, React, TypeScript, Ant Design X
-   **Backend**: Python 3.11+, FastAPI, Uvicorn
-   **Database**: Weaviate (Vector DB)
-   **Deployment**: Vercel Ready

## 🏁 Quick Start

### Prerequisites

-   Node.js & pnpm
-   Python 3.11 (Recommended)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/ASCK.git
    cd ASCK
    ```

2.  **Initialize the project**
    This script will install all dependencies for both frontend and backend, and set up environment variables.
    ```bash
    ./asck_init.sh
    ```

### Running the App

Start both frontend and backend services with a single command:

```bash
./asck_start.sh
```

-   **Frontend**: http://localhost:5173
-   **Backend API**: http://localhost:8000/docs

To stop the services:

```bash
./asck_stop.sh
```

## ☁️ Deployment

This project is optimized for deployment on **Vercel**.

1.  Push your code to GitHub.
2.  Import the project into Vercel.
3.  Configure the build settings:
    -   **Root Directory**: `.` (Leave empty)
    -   **Build Command**: `cd frontend && pnpm install && pnpm build`
    -   **Output Directory**: `frontend/dist`
4.  Add your environment variables in the Vercel dashboard.
5.  Deploy!

## 📄 License

[MIT](LICENSE)
