# -*- coding: utf-8 -*-
"""
작성자: jiw0n0107@yahoo.com
날짜: 2025-05-27
설명: 사용자 이름 기반 로그 데이터를 처리하는 데이터 파이프라인
"""

import pandas as pd
from pathlib import Path

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def transform_data(df):
    df['day'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

def run_pipeline():
    input_path = "../raw_data/user_log.csv"
    output_path = "../cleaned_data/cleaned_user_log.csv"

    df = load_data(input_path)
    df = clean_data(df)
    df = transform_data(df)
    save_data(df, output_path)

if __name__ == "__main__":
    run_pipeline()
