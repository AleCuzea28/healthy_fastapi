from fastapi import APIRouter

import json
import logging
import random
import sys
from datetime import datetime
from typing import Iterator

import asyncio
from fastapi.responses import HTMLResponse, StreamingResponse, FileResponse
from fastapi.requests import Request

import plotly.graph_objs as go
import yfinance as yf


# from PIL import Image

finance_router = APIRouter(prefix="/finance", tags=["finance"])


@finance_router.get("/chart-data/{tickers1}/{tickers2}")
async def chart_data(tickers_f1, tickers_f2, period_f, interval_f):
    data = yf.download(
        tickers=[tickers_f1, tickers_f2],
        period=period_f,
        interval=interval_f,
        rounding=True,
    )

    fig = go.Figure()
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name="market data",
        )
    )
    fig.update_layout(title=f"{tickers_f} share price", yaxis_title="Stock Price (USD)")
    # fig.update_xaxes(
    #     rangeslider_visible=True,
    #     rangeselector=dict(
    #         buttons=list(
    #             [
    #                 dict(count=15, label="15m", step="minute", stepmode="backward"),
    #                 dict(count=45, label="45m", step="minute", stepmode="backward"),
    #                 dict(count=1, label="1h", step="hour", stepmode="backward"),
    #                 dict(count=6, label="6h", step="hour", stepmode="backward"),
    #                 dict(step="all"),
    #             ]
    #         )
    #     ),
    # )
    fig.write_image("imggg.jpg")

    return FileResponse("imggg.jpg")


# random.seed()  # Initialize the random number generator


# async def generate_random_data(request: Request) -> Iterator[str]:
#     """
#     Generates random value between 0 and 100

#     :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
#     """
#     print("Heeeeeeeeeeeeeeei")
#     while True:
#         json_data = json.dumps(
#             {
#                 "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "value": random.random() * 100,
#             }
#         )
#         yield f"data:{json_data}\n\n"
#         await asyncio.sleep(1)


# @finance_router.get("/chart-data")
# async def chart_data(request: Request):
#     response = StreamingResponse(
#         generate_random_data(request), media_type="text/event-stream"
#     )
#     # response.headers["Cache-Control"] = "no-cache"
#     # response.headers["X-Accel-Buffering"] = "no"
#     return response
