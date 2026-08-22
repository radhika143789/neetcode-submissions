class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local,domain = email.split('@')
            local = local.split('+')
            local = local[0].replace('.','')
            unique.add(local + '@' + domain)
        print(unique)
        return len(unique)
        