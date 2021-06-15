import twint

# Configure
c = twint.Config()
c.Username = "niall_boylan"
c.Search = "today"

# Run
twint.run.Search(c)