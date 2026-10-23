
from urllib.parse import urlsplit

# Websites that our program should block
BLOCKED_SITES = {
    "example.com",
    "blocked.test",
    "youtube.com",
}


def get_domain(url):
    """Extract the hostname from a URL."""
    if "://" not in url:
        url = "https://" + url

    parsed_url = urlsplit(url)
    domain = parsed_url.hostname 

    if domain is None:
        return None

    return domain.lower().rstrip(".")


def is_blocked(domain):
    """Check whether a domain matches our blocklist."""
    if domain is None:
        return False

    for blocked_site in BLOCKED_SITES:
        if domain == blocked_site:
            return True

        if domain.endswith("." + blocked_site):
            return True

    return False


def main():
    print("=== Website Guardian ===")
    print("Type 'quit' to exit.")

    while True:
        url = input("\nEnter a website: ").strip()

        if url.lower() == "quit":
            print("Goodbye!")
            break

        domain = get_domain(url)

        if domain is None:
            print("Invalid website address.")
        elif is_blocked(domain):
            print(f"BLOCKED: {domain}")
        else:
            print(f"ALLOWED: {domain}")


if __name__ == "__main__":
    main()
