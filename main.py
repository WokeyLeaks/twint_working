import twint

# Configure
c = twint.Config()
c.Username = "niall_boylan"
c.Search = "today"

# Run it
twint.run.Search(c)