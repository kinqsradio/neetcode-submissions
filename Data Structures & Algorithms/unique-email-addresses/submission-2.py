class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails or len(emails) == 0: return 0

        # HashSet
        unique = set()

        # Loop over emails
        for e in emails:
            local, domain = e.split('@') # split into 2 parts before and after @
            local = local.split("+")[0] # retrieve first part before +
            local = local.replace(".", "") # remove .
            unique.add((local, domain))

        return len(unique)