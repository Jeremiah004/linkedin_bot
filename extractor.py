from pypdf import PdfReader
import re


class ResumeParser():
    def __init__(self, file_path: str)-> None:
        self.file_path = file_path
        self.text = self.load_text(file_path)
        self.data = {}
    
    def load_text(self):
        reader = PdfReader(self.file_path)
        text = ""
        for i in range(PdfReader.get_num_pages(reader)):
            page = reader.pages[i]
            text += page.extract_text()
        return text
        
    def extract_personal_information(self) ->dict:
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"(\+\d{1,3})?[-.\s]??(\d{3}[-.\s]??\d{3}[-.\s]??\d{4})"
        linkedin_pattern = r"(https?://)?(www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+"
        github_pattern = r"(https?://)?(www\.)?github\.com/[a-zA-Z0-9_-]+"
        name_pattern = r"(?:NAME[:\s]*)?([A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s[A-Z][a-z]+)"
        personal_info = {}
        email = re.search(email_pattern, self.text)
        phone = re.search(phone_pattern, self.text)
        linkedin = re.search(linkedin_pattern, self.text)
        github = re.search(github_pattern, self.text)
        name = re.search(name_pattern, self.text)
        personal_info["email"] = email if email else None
        personal_info["phone_number"] = phone if phone else None
        personal_info["linkedin"] = linkedin if linkedin else None
        personal_info['github'] = github if github else None
        personal_info['name'] = name if name else None
        
        return personal_info
    def extract_educational(self) ->dict:
        pass

    def extract_experience(self) ->dict:
        pass

    def extract_projects(self) ->dict:
        pass

    def skills(self) -> dict:
        pass
    def extract_certification(self) ->dict:
        pass




with pdfplumber.open(r"C:\Users\JERRY\Music\linkedIn_auto_jobs_applier_with_AI-main\Andrew Okolo Resume Koo.pdf") as file:
    first_page = file.pages[0]
    print(first_page.chars[0])