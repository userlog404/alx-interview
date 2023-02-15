import sys

# Initialize variables
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Read input line by line
try:
    line_count = 0
    for line in sys.stdin:
        # Split line into components
        parts = line.strip().split()
        if len(parts) != 6:
            # Line is not in expected format, skip it
            continue
        if parts[0].find('.') == -1:
            # IP address is not valid, skip line
            continue
        if parts[2][0] != '"':
            # Request is not in expected format, skip line
            continue
        if parts[3] not in status_code_counts:
            # Status code is not an expected value, skip line
            continue
        if not parts[5].startswith('('):
            # File size is not in expected format, skip line
            continue
        # Parse file size and status code
        file_size = int(parts[5][1:-1])
        status_code = int(parts[3])
        # Update statistics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            # Print statistics after every 10 lines
            print("Total file size: File size: %d" % total_file_size)
            for status_code in sorted(status_code_counts.keys()):
                if status_code_counts[status_code] > 0:
                    print("%d: %d" % (status_code, status_code_counts[status_code]))
except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print("Total file size: File size: %d" % total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print("%d: %d" % (status_code, status_code_counts[status_code]))
