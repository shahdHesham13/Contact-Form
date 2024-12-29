
## Simple Contact Form

**Week 3 Assesment** <br>
Contact page allows users to send messages, which are delivered to your email address. The contact form includes fields for the user's name, email, and message.<br>
This task will help them understand form handling, validation, and sending emails.



 **Configure email settings:**

   In your `settings.py`, you'll need to add the following email configuration to enable sending emails via SMTP:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.your-email-provider.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@example.com'  # Your email address
   EMAIL_HOST_PASSWORD = 'your-email-password'  # Your email password or app-specific password
   DEFAULT_FROM_EMAIL = 'your-email@example.com'
   CONTACT_EMAIL = 'recipient@example.com' # Where contact form submissions will be sent
   ```

   **Note:** Make sure to replace the placeholders with your actual email provider details.


 **Visit the application:**
   Navigate to `http://127.0.0.1:8000` in your web browser to interact with the application.
