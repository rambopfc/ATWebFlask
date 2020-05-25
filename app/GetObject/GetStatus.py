def get_status(i):
    switcher = {
        27: "Needs Hardware Ordered",
        24: "Needs Scheduling",
        26: "Pre-Work (In Progress)",
        25: "Pre-Work (Needed)",
        23: "Waiting Payment",
        28: "Waiting Retail",
        21: "Waiting Technician",
        1: "New",
        13: "Waiting Approval",
        10: "Dispatched",
        15: "Change Order",
        19: "Customer Note Added",
        8: "In Progress",
        11: "Escalate",
        9: "Waiting Materials",
        7: "Waiting Customer",
        12: "Waiting Vendor",
        20: "Waiting Fix Verification",
        17: "On Hold",
        14: "Billed",
        16: "Inactive",
        5: "Complete",
        22: "NEEDS ATTENTION",
        29: "Waiting Sales",
        30: "Needs Follow Up",
        31: "Needs Planning",
        32: "Waiting PIN Code",
    }
    return switcher.get(i, "Invalid Status")
