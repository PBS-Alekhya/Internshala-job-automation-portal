import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sqlite3

def apply_for_job(job_url, resume_path, user_id, internshala_email, internshala_password):
    # Convert relative path to absolute path
    resume_path = os.path.abspath(resume_path)
    print(f"Resume path: {resume_path}")
    
    # Check if the file exists
    if not os.path.exists(resume_path):
        raise FileNotFoundError(f"Resume file not found at: {resume_path}")
    
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()  # Use appropriate driver
    driver.get("https://internshala.com/login/user")  # Go to Internshala homepage
    print("Navigated to Internshala login page")
    
    try:
        # Log in to Internshala
        # print("Logging in to Internshala...")
        # login_link = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        # )
        # login_link.click()
        # print("Clicked login link")
        
        # Wait for the login modal to appear
        time.sleep(2)
        email_field = WebDriverWait(driver, 13).until(
            EC.element_to_be_clickable((By.NAME, "email"))
        )
        time.sleep(3)
        email_field.send_keys(internshala_email)
        print("Entered email")
        password_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        time.sleep(random.uniform(2, 4))
        password_field.send_keys(internshala_password)
        print("Entered password")
        
        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "login_submit"))
        )
        time.sleep(random.uniform(2, 7))
        login_button.click()
        print("Clicked login button")
        
        # Wait for login to complete
        WebDriverWait(driver, 15).until(
            EC.url_contains("internshala.com/student/dashboard")
        )
        print("Logged in successfully")
        
        # Navigate to the job URL
        print(f"Navigating to job URL: {job_url}")
        driver.get(job_url)
        
        # Wait for the "Apply Now" button to be clickable
        print("Waiting for 'Apply Now' button...")
        apply_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "apply_now_button"))  # Update the selector
        )
        apply_now_button.click()
        print("Clicked 'Apply Now' button")
        
        
        # Wait for the "Proceed to Application" button to be clickable
        print("Waiting for 'Proceed to Application' button...")
        proceed_button = WebDriverWait(driver, 15).until(
            # EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-large education_incomplete proceed-btn")) 
            EC.element_to_be_clickable((By.TAG,"button")) 
            # Ec.element_to_be_clicksable(())
            
        )
        proceed_button.click()
        print("Clicked 'Proceed to Application' button")
        
        # Wait for the application form to load
        # print("Waiting for application form to load...")
        # resume_input = WebDriverWait(driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "resume_input"))  # Update the selector
        # )
        # # resume_input.send_keys(resume_path)
        # print("Uploaded resume")
        
        # Fill out the application form (if required)
        # print("Filling out the application form...")
        # name_field = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "name_field"))  # Update the selector
        # )
        # name_field.send_keys("John Doe")
        # print("Entered name")
        
        # email_field = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "email_field"))  # Update the selector
        # )
        # email_field.send_keys("john@example.com")
        # print("Entered email")
        
        # Click the "Submit" button
        print("Clicking 'Submit' button...")
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit_button"))  # Update the selector
        )
        submit_button.click()
        print("Clicked 'Submit' button")
        
        # Wait for the application to complete
        WebDriverWait(driver, 10).until(
            EC.url_contains("internshala.com/application-success")
        )
        print("Application submitted successfully")
        
        # Extract job details (if needed)
        job_title = driver.find_element(By.ID, "job_title").text
        company_name = driver.find_element(By.ID, "company_name").text
        print(f"Job Title: {job_title}, Company: {company_name}")
        
        # Save job details to database
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO jobs (user_id, job_title, company_name, applied_date) VALUES (?, ?, ?, ?)',
                     (user_id, job_title, company_name, time.strftime('%Y-%m-%d')))
        conn.commit()
        conn.close()
        print("Job details saved to database")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot('error_screenshot.png')  # Take a screenshot
    finally:
        driver.quit()
        print("WebDriver closed")