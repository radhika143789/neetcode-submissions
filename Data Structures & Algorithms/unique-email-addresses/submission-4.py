class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        arr = set()
        for email in emails:
            local_name = email.split('@')[0]
            local_name = local_name.split("+")[0]
            local_name = "".join(local_name.split('.'))
            arr.add(local_name+email.split("@")[-1])
        return len(arr)