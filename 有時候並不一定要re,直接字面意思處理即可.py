class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            name, domain = email.split('@')
    #         print(name,domain)
            if "+" in name:
                name = name[:name.find('+')].replace('.', '')
            else:
                name = name.replace(".","")
            email_set.add(name + '@' + domain)
        return len(email_set)
