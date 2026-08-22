class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local ,domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            
            # 4. Combine them back and add to our set
            clean_email = local + '@' + domain
            unique_emails.add(clean_email)
            
        # 5. The number of unique emails is the size of the set
        return len(unique_emails)
        