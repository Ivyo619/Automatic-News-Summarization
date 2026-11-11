
# ==========================================
# AUTOMATIC NEWS SUMMARIZATION
# DistilBART NLP ENGINE
# Stage 4: Chunk-Based Summarization
# ==========================================

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from preprocessing import (
    preprocess_text,
    count_tokens,
    split_into_chunks
)

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

device = torch.device("cpu")


# 1. LOAD MODEL

def load_model():

    print("Loading DistilBART model...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    model.to(device)
    model.eval()

    print("Model loaded successfully!")

    return tokenizer, model


# 2. SUMMARY LENGTH SETTINGS

SUMMARY_SETTINGS = {

    "short": {
        "max_length": 80,
        "min_length": 20
    },

    "medium": {
        "max_length": 130,
        "min_length": 40
    },

    "long": {
        "max_length": 180,
        "min_length": 60
    }

}


# 3. WORD COUNT

def count_words(text):

    return len(text.split())


# 4. SUMMARIZE INDIVIDUAL CHUNK

def summarize_chunk(text, tokenizer, model, settings):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        summary_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=settings["max_length"],
            min_length=settings["min_length"],
            num_beams=2,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

    return tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )


# 5. COMPLETE SUMMARIZATION ENGINE

def generate_summary(
    article,
    tokenizer,
    model,
    summary_length="medium"
):

    if not isinstance(article, str) or not article.strip():

        raise ValueError("Please enter a valid news article.")

    if summary_length not in SUMMARY_SETTINGS:

        raise ValueError("Choose short, medium or long.")

    # Preprocess article
    article = preprocess_text(article)

    settings = SUMMARY_SETTINGS[summary_length]

    total_tokens = count_tokens(article, tokenizer)

    print("Input Tokens:", total_tokens)

    # CASE 1: Single article
    if total_tokens <= 900:

        print("Processing single article...")

        return summarize_chunk(
            article,
            tokenizer,
            model,
            settings
        )

    # CASE 2: Long article
    print("Processing using chunk-based summarization...")

    chunks = split_into_chunks(
        article,
        tokenizer,
        chunk_size=850
    )

    print("Number of chunks:", len(chunks))

    intermediate_summaries = []

    for index, chunk in enumerate(chunks):

        print(
            f"Summarizing chunk {index + 1}/{len(chunks)}..."
        )

        chunk_summary = summarize_chunk(
            chunk,
            tokenizer,
            model,
            SUMMARY_SETTINGS["medium"]
        )

        intermediate_summaries.append(chunk_summary)

    # Combine summaries
    combined_summary = " ".join(intermediate_summaries)

    # Reduce if still too long
    rounds = 0

    while count_tokens(combined_summary, tokenizer) > 900:

        rounds += 1

        if rounds > 5:

            raise RuntimeError(
                "Could not reduce combined summary."
            )

        print("Performing another summarization pass...")

        smaller_chunks = split_into_chunks(
            combined_summary,
            tokenizer,
            chunk_size=850
        )

        smaller_summaries = []

        for chunk in smaller_chunks:

            smaller_summaries.append(
                summarize_chunk(
                    chunk,
                    tokenizer,
                    model,
                    SUMMARY_SETTINGS["medium"]
                )
            )

        combined_summary = " ".join(smaller_summaries)

    # Final summary
    print("Generating final summary...")

    final_summary = summarize_chunk(
        combined_summary,
        tokenizer,
        model,
        settings
    )

    return final_summary


# 6. SUMMARY STATISTICS

def calculate_statistics(article, summary):

    original_words = count_words(article)

    summary_words = count_words(summary)

    if original_words > 0:

        compression_ratio = (
            (1 - summary_words / original_words) * 100
        )

    else:

        compression_ratio = 0

    return {

        "original_word_count": original_words,

        "summary_word_count": summary_words,

        "compression_ratio": round(compression_ratio, 2)

    }


print("Summarizer module loaded successfully!")
