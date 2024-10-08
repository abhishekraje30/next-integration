import frappe

@frappe.whitelist()
def trigger_next_reset_password(email, reset_link, sent_by):
    user = frappe.get_doc("User", email)
    template = frappe.render_template('/templates/nextauth_reset_password.html', {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "link": reset_link,
        "sent_by": sent_by
    })
    frappe.sendmail(
        recipients=email,
        subject="Password Reset",
        message=template,
        now=True,
    )
    return "Password reset link has been sent to your email."

@frappe.whitelist()
def trigger_next_user_verification(email, verification_link, sent_by):
    user = frappe.get_doc("User", email)
    template = frappe.render_template('/templates/nextauth_email_verification.html', {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "verification_link": verification_link,
        "sent_by": sent_by
    })
    frappe.sendmail(
        recipients=email,
        subject="Verify your email",
        message=template,
        now=True,
    )
    return "Email verification link has been sent to your email."