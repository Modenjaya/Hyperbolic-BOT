# Hyperbolic Automated Chat Bot

A Python script that automatically generates random questions and sends them to the Hyperbolic API to get responses from the Meta-Llama-3.1-8B-Instruct model.

## Features

- Generates random questions across various topics
- Sends requests to the Hyperbolic API
- Configurable response parameters
- Random timing between requests (60-120 seconds)
- Graceful shutdown with CTRL+C

## Prerequisites

- Python 3.x
- `requests` library
- Hyperbolic API key with sufficient balance

## Installation

1. Clone this repository or download the script
2. Install the required package:

```
pip install requests
```

3. Add your API key to the script by replacing `YOUR_API_KEY_HERE` in the `HEADERS` dictionary

## Getting an API Key

1. Visit [Hyperbolic Settings Page](https://app.hyperbolic.xyz/settings) to obtain your API key
2. Ensure you have sufficient balance in your account to make API requests
3. Copy your API key and paste it in the script

## Usage

Simply run the script:

```
python main.py
```

The script will:

1. Generate a random question
2. Send it to the Hyperbolic API
3. Display the model's response
4. Wait for a random period (60-120 seconds)
5. Repeat the process

To stop the script, press CTRL+C.

## Customization

You can modify the following parts of the script:

- `topics`: Add or remove topics for question generation
- `actions`: Customize the question formats
- `specifics`: Add context variations to questions
- API parameters: Adjust temperature, tokens, and other model settings

## API Configuration

The script is configured to use:

- Model: meta-llama/Meta-Llama-3.1-8B-Instruct
- Max tokens: 2048
- Temperature: 0.7
- Top_p: 0.9

You can adjust these parameters in the `send_chat_request()` function.
