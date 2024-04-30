# online_wordlist
Now no need to download Wordlists and no need to create wordlists... Here is my Program which Instantly uses Wordlists from the WEB and use it to crack the passwords.
<h2> Installation </h2>
<p>
You can install this amazing tool in Linux or Termux Environment
</p>
<b><u>commands:</b></u>
<p> <b> sudo apt install hashcat </b> </p>

<p> Now You are ready to use this tool </p>
<h2> Syntax and Usage: </h2>
<p>
<b>
python online_wordlist.py (wordlist_urls_file) (pipe_commands) (session_file_for_resume)
</b>
</p>

<u> EXAMPLE: </u> python online_wordlist.py wordlist.url "hashcat -a 22000 -m 3 example.hash" session1
<h1> THANKS for using my PROGRAM, Don't Forget to STAR this </h1>
