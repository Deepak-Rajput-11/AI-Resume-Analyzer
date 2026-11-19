from ml.text_preprocessor import clean_text


def process_job_description(jd_text):
    cleaned_jd = clean_text(jd_text)

    return cleaned_jd
