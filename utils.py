def complex_processing(data):
    """
    Complex function with issues for Celesta to find
    """
    results = []
    
    # Deep nesting
    for item in data:
        if item.active:
            for sub in item.subitems:
                for detail in sub.details:
                    for value in detail.values:
                        results.append(value)
    
    # TODO: refactor this
    # FIXME: add caching
    
    # Debug code
    print("Processing complete")
    console.log("Debug info")
    
    return results
