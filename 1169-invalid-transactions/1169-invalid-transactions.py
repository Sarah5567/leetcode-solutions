class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_indices = set()
        
        parsed_transactions = []
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            parsed_transactions.append((name, int(time), int(amount), city, i))
            
        parsed_transactions.sort(key=lambda x: x[1])
        
        transactions_by_name = collections.defaultdict(lambda: collections.defaultdict(list))
        
        for name, time, amount, city, original_idx in parsed_transactions:
            if amount > 1000:
                invalid_indices.add(original_idx)
            
            for other_city, history in transactions_by_name[name].items():
                if other_city != city:
                    for prev_time, prev_idx in history:
                        if time - prev_time <= 60:
                            invalid_indices.add(original_idx)
                            invalid_indices.add(prev_idx)
            
            transactions_by_name[name][city].append((time, original_idx))
            
        return [transactions[i] for i in invalid_indices]