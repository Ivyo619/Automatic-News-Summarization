# AI Powered News Summarization System

## 1. Project Description

The **AI Powered News Summarization System** is a web-based application developed using Python and Natural Language Processing (NLP). It automatically extracts news articles from URLs and generates concise summaries using the pretrained DistilBART Transformer model.

The main purpose of this project is to reduce the time required to read lengthy news articles by converting them into shorter, meaningful summaries while retaining the important information.

The application uses Streamlit to provide an interactive user interface where users can enter a news article URL, generate its summary, view the original article, check summary statistics and download the generated summary.

## 2. Technologies Used

- **Python:** Core programming language.
- **Streamlit:** Development of the interactive web application.
- **PyTorch:** Deep learning framework used to execute the summarization model.
- **Hugging Face Transformers:** Loading and implementing the pretrained model.
- **DistilBART:** Transformer-based abstractive text summarization model.
- **Trafilatura:** Extracting article content from news websites.
- **Regular Expressions (Regex):** Cleaning and preprocessing text.
- **HTML:** Handling HTML tags and entities.

## 3. Model Information

The project uses the pretrained model:

`sshleifer/distilbart-cnn-12-6`

DistilBART is a Transformer-based model designed for text summarization. It identifies important information from the input article and generates a shorter, readable version.

The model is downloaded automatically from Hugging Face during its first execution.

## 4. Project Structure

```text
Automatic-News-Summarization/
│
├── app.py
├── summarizer.py
├── preprocessing.py
├── article_extractor.py
├── evaluation.py
├── main.py
├── requirements.txt
├── README.md
│
├── outputs/
│
└── .venv/
```

### Description of Files

- **app.py:** Main Streamlit application that provides the user interface and connects all the processing modules.
- **summarizer.py:** Loads the DistilBART model and generates summaries from extracted article text.
- **preprocessing.py:** Performs text cleaning, token counting and text chunking.
- **article_extractor.py:** Contains article extraction functionality.
- **evaluation.py:** Contains summary evaluation functionality.
- **main.py:** Provides standalone execution and testing of the summarization system.
- **requirements.txt:** Contains the Python libraries required to run the project.
- **outputs/:** Stores generated output files.

## 5. Working Methodology

The system follows these steps:

1. **URL Input:** The user enters the URL of a publicly accessible news article.
2. **Article Extraction:** Trafilatura fetches the webpage and extracts the main article content.
3. **Text Preprocessing:** Unnecessary HTML tags, URLs and extra spaces are removed.
4. **Tokenization:** The extracted text is converted into tokens using the DistilBART tokenizer.
5. **Text Processing:** Long articles can be divided into smaller chunks to handle the model's input token limitations.
6. **Summary Generation:** The DistilBART model processes the text and generates an abstractive summary.
7. **Statistics Calculation:** The system calculates the original word count, summary word count and compression ratio.
8. **Result Display:** The original article and generated summary are displayed through the Streamlit interface.
9. **Download:** Users can download the generated summary as a text file.

## 6. Installation and Execution Process

Follow the steps below to execute the project on a Windows system.

### Step 1: Install Python

Install Python 3.11 or a compatible Python version.

Verify the installation:

```bash
python --version
```

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

Open the integrated terminal.

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Required Libraries

Install all project dependencies using:

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

Execute the following command in the terminal:

```bash
python -m streamlit run app.py
```

### Step 7: Open the Web Application

After successful execution, Streamlit provides a local URL:

```text
http://localhost:8501
```

Open the URL in a web browser to access the application.

## 7. How to Use the Application

1. Open the AI Powered News Summarization System in your browser.
2. Enter the URL of a publicly accessible news article.
3. Click on the **Generate Summary** button.
4. Wait while the system extracts the article and processes it using DistilBART.
5. View the original article and AI-generated summary.
6. Check the summary statistics, including:
   - Original Word Count
   - Summary Word Count
   - Compression Ratio
7. Click on **Download Summary** to save the generated summary as a `.txt` file.

## 8. Output

The application generates the following results:

- Extracted original news article.
- AI-generated summarized text.
- Original article word count.
- Summary word count.
- Compression ratio.
- Downloadable summary file.

## 9. System Requirements

- Operating System: Windows 10/11 or compatible OS.
- Programming Language: Python 3.11 or compatible version.
- IDE: Visual Studio Code.
- RAM: 8 GB recommended.
- Internet Connection: Required for article extraction and initial model download.
- Processing: CPU-based model execution is supported.

## 10. Limitations

- Some news websites may restrict automated article extraction.
- Summary generation may take time on CPU-based systems.
- The generated summary may occasionally miss certain contextual details.
- The system requires an internet connection to fetch online articles.

## 11. Conclusion

The AI Powered News Summarization System demonstrates how Natural Language Processing and Transformer-based deep learning models can be used to automate news summarization.

By integrating article extraction, text preprocessing, DistilBART and Streamlit, the project provides an efficient way to convert lengthy news articles into concise and meaningful summaries.

The application simplifies access to information, reduces reading time and demonstrates the practical implementation of Artificial Intelligence in text processing.

---

**Project Domain:** Artificial Intelligence and Natural Language Processing  
**Model:** DistilBART  
**Framework:** PyTorch and Hugging Face Transformers  
**Frontend:** Streamlit  
**Language:** Python
