def process_user_data(users):
    """
    Process user data - intentionally has issues for Celesta to find!
    """
    results = []
    
    # Deep nesting issue (will trigger static analyzer)
    for user in users:
        if user.active:
            for account in user.accounts:
                for transaction in account.transactions:
                    for item in transaction.items:
                        for detail in item.details:
                            results.append(detail.value)
    
    # TODO: optimize this function
    # TODO: add error handling
    
    # Debug code left in (should be removed!)
    print(f"Processed {len(users)} users")
    console.log("Debug: results ready")
    
    # Long line that exceeds 120 characters
    some_very_long_variable_name_that_is_way_too_long_for_proper_code_quality_standards = "This line is too long and should be wrapped"
    
    return results


def very_long_function_name_that_should_be_shorter_and_more_descriptive():
    """
    This function is intentionally too long for code quality checks.
    """
    data = []
    for i in range(100):
        for j in range(50):
            data.append(i + j)
    
    processed = []
    for item in data:
        for sub_item in data:
            processed.append(item + sub_item)
    
    return processed


class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        # Missing validation
        self.users.append(user)
        
        # FIXME: Should check for duplicates
    
    def find_user(self, user_id):
        # Could use better algorithm
        for user in self.users:
            if user.id == user_id:
                return user
        return None
