
# ==========================================================
# AUTOMATIC NEWS SUMMARIZATION SYSTEM
# Stage 6: Complete System Integration
# ==========================================================

import os
from datetime import datetime

from article_extractor import extract_article, save_article

from summarizer import (
    generate_summary,
    calculate_statistics
)


# ----------------------------------------------------------
# 1. APPLICATION HEADER
# ----------------------------------------------------------

def display_header():

    print("\n" + "=" * 60)
    print("       AUTOMATIC NEWS SUMMARIZATION SYSTEM")
    print("=" * 60)

    print("Powered by DistilBART and Natural Language Processing")


# ----------------------------------------------------------
# 2. SELECT SUMMARY LENGTH
# ----------------------------------------------------------

def get_summary_length():

    print("\nSelect Summary Length:")

    print("1. Short")
    print("2. Medium")
    print("3. Long")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    options = {
        "1": "short",
        "2": "medium",
        "3": "long"
    }

    if choice not in options:

        print("Invalid choice. Medium selected by default.")

        return "medium"

    return options[choice]


# ----------------------------------------------------------
# 3. SAVE FINAL SUMMARY
# ----------------------------------------------------------

def save_summary(article_data, summary, statistics, length):

    os.makedirs("outputs", exist_ok=True)

    file_path = os.path.join(
        "outputs",
        "final_summary.txt"
    )

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")

        file.write("AUTOMATIC NEWS SUMMARIZATION REPORT\n")

        file.write("=" * 60 + "\n\n")

        file.write("TITLE: " + article_data["title"] + "\n")

        file.write("AUTHOR: " + article_data["author"] + "\n")

        file.write("DATE: " + article_data["date"] + "\n\n")

        file.write("SUMMARY TYPE: " + length.upper() + "\n\n")

        file.write("GENERATED SUMMARY:\n\n")

        file.write(summary + "\n\n")

        file.write("=" * 60 + "\n")

        file.write("SUMMARY STATISTICS\n\n")

        file.write(
            "Original Word Count: "
            + str(statistics["original_word_count"])
            + "\n"
        )

        file.write(
            "Summary Word Count: "
            + str(statistics["summary_word_count"])
            + "\n"
        )

        file.write(
            "Compression Ratio: "
            + str(statistics["compression_ratio"])
            + "%\n"
        )

        file.write(
            "\nGenerated On: "
            + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        )

    return file_path


# ----------------------------------------------------------
# 4. MAIN APPLICATION
# ----------------------------------------------------------

def main():

    display_header()

    # Get news article URL
    news_url = input(
        "\nEnter the News Article URL: "
    ).strip()

    if not news_url:

        print("\nError: News URL cannot be empty.")

        return

    # Select summary length
    summary_length = get_summary_length()

    try:

        # ----------------------------------------------
        # STEP 1: ARTICLE EXTRACTION
        # ----------------------------------------------

        print("\n[STEP 1] Extracting news article...")

        article_data = extract_article(news_url)

        article = article_data["article"]

        print("\nArticle extracted successfully!")

        print("Title:", article_data["title"])

        print("Author:", article_data["author"])

        print("Publication Date:", article_data["date"])

        print("Article Words:", len(article.split()))

        # Save extracted article
        save_article(article_data)

        # ----------------------------------------------
        # STEP 2: AI SUMMARIZATION
        # ----------------------------------------------

        print("\n[STEP 2] Starting AI summarization...")

        print("Selected Length:", summary_length.upper())

        summary = generate_summary(
            article,
            summary_length=summary_length
        )

        # ----------------------------------------------
        # STEP 3: SUMMARY STATISTICS
        # ----------------------------------------------

        print("\n[STEP 3] Calculating summary statistics...")

        statistics = calculate_statistics(
            article,
            summary
        )

        # ----------------------------------------------
        # STEP 4: DISPLAY FINAL SUMMARY
        # ----------------------------------------------

        print("\n" + "=" * 60)

        print("              GENERATED NEWS SUMMARY")

        print("=" * 60)

        print("\n", summary)

        print("\n" + "=" * 60)

        print("                SUMMARY STATISTICS")

        print("=" * 60)

        print(
            "Original Word Count:",
            statistics["original_word_count"]
        )

        print(
            "Summary Word Count:",
            statistics["summary_word_count"]
        )

        print(
            "Compression Ratio:",
            str(statistics["compression_ratio"]) + "%"
        )

        # ----------------------------------------------
        # STEP 5: SAVE FINAL REPORT
        # ----------------------------------------------

        print("\n[STEP 4] Saving final report...")

        report_path = save_summary(
            article_data,
            summary,
            statistics,
            summary_length
        )

        print("\nFinal summary saved successfully!")

        print("Report Location:", report_path)

        print("\n" + "=" * 60)

        print("       NEWS SUMMARIZATION COMPLETED!")

        print("=" * 60)

    except Exception as error:

        print("\nAPPLICATION ERROR:", error)

        print(
            "\nPlease check the URL, internet connection "
            "and article extraction."
        )


# ----------------------------------------------------------
# 5. APPLICATION ENTRY POINT
# ----------------------------------------------------------

if __name__ == "__main__":

    main()
