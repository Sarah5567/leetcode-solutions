class Solution:
    def simplifyPath(self, path: str) -> str:
        entries = []
        for ch in path:
            if ch == '/':
                if entries and entries[-1] == '.':
                    entries.pop()
                elif entries and entries[-1] == '..':
                    entries.pop()
                    if entries:
                        entries.pop()

                if not entries or entries[-1]:
                    entries.append('')

            else:
                entries[-1] += ch

        if entries and entries[-1] in ['.', '']:
            entries.pop()
        elif entries and entries[-1] == '..':
            entries.pop()
            if entries:
                entries.pop()

        return '/' + '/'.join(entries)
