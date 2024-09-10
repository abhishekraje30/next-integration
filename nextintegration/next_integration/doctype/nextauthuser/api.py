import frappe

@frappe.whitelist()
def trigger_next_reset_password(email):
    user = frappe.get_doc("User", email)
    next_integration_user = frappe.get_doc("NextAuthUser", email)
    template = frappe.render_template('/templates/nextauth_reset_password.html', {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "link": "reset-password",
        "created_by": "Administrator"
    })
    frappe.sendmail(
        recipients=email,
        subject="Password Reset",
        message=template,
        now=True,
    )
    return "Password reset link has been sent to your email."