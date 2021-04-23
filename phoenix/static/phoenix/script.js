document.addEventListener('DOMContentLoaded', function(){
   getquestnames()
   initialhighlight()
   document.querySelectorAll('button').forEach(item => {
      item.addEventListener('click', () => {
         let data = {
            "node" : item.innerText
         }
         if(item.className =="greenbox" && item.parentElement.parentElement.parentElement.children[0].id =="image"){
            console.log("nice")
            fetch('/getquests', {
               method:'POST',
               body : JSON.stringify(data),
               headers: {"X-CSRFToken" : item.dataset.csrf}
            })
            .then(response => response)
            .then(result => {
               buildquestlist()
               highlightancestors(item)
            })
         }else if(item.className =="greenbox"){
            console.log("nice")
            fetch('/getquests', {
               method:'POST',
               body : JSON.stringify(data),
               headers: {"X-CSRFToken" : item.dataset.csrf}
            })
            .then(response => response)
            .then(result => {
               buildquestlist()
               highlightancestors(item)
            })
         }else{
            fetch('/questroute', {
               method: 'POST',
               body : JSON.stringify(data),
               headers: {"X-CSRFToken" : item.dataset.csrf}
            })
            .then(response => response.json())
            .then(result => {
               buildquestlist()
               highlightancestors(item)
            })
         }
      });
   });

   // for(i=0; i<closebtns.length; i++){
   //    closebtns[i].addEventListener("click", function() {
   //       this.parentElement.style.display = 'none';
   //    })
   // }
});

function initialhighlight() {
   fetch('/getquests')
   .then(response => response.json())
   .then(result => {
      console.log(result)
      for(x in result){
         if (result[x].name){
            doc = document.getElementById(result[x].name)
            doc.className = "greenbox"
         }else if(result[x].complete){
            doc = document.getElementById(result[x].complete)
            doc.className = "bluebox"
         }
         // if (doc.parentElement.parentElement.parentElement.children[0].id != "image"){
         //    doc=doc.parentElement.parentElement.parentElement.children[0]
         //    while(doc.id != "image"){
         //       doc.className="bluebox"
         //       doc=doc.parentElement.parentElement.parentElement.children[0]
         //    }
         // }
      }
   })
}

function removehighlight(element) {
   initialhighlight()
   // doc = document.getElementById(element.innerHTML)
   // doc.classList.remove("greenbox")
   // if (doc.parentElement.parentElement.parentElement.children[0].id != "image"){
   //    doc=doc.parentElement.parentElement.parentElement.children[0]
   //    while(doc.id != "image"){
   //       doc.classList.remove("bluebox")
   //       doc=doc.parentElement.parentElement.parentElement.children[0]
   //    }
   // }
}


function buildquestlist() {
   fetch('/questroute', {
      method: 'GET',
   })
   .then(response => response.json())
   .then(result => {
      a=document.getElementById('questsfir')
      a.innerHTML=""
      resoolt = result[1]
      for(x in resoolt){
         if(document.getElementById("quest" + resoolt[x].quest) == null){
            var questli=document.createElement("li")
            var itemul=document.createElement("ul")
            var h3 = document.createElement("strong")
            var questtext = document.createTextNode(resoolt[x].quest)
            itemul.setAttribute("id", "quest" + resoolt[x].quest)
            a.appendChild(questli)
            h3.appendChild(questtext)
            questli.appendChild(h3)
            questli.appendChild(itemul)
         }
         var text = document.createTextNode(resoolt[x].num + "x " + resoolt[x].item)
         var li=document.createElement("li")
         li.appendChild(text)
         document.getElementById("quest" + resoolt[x].quest).appendChild(li)
      }
      //build Current Quest list
      a=document.getElementById("questlistul")
      a.innerHTML=""
      roosalt = result[0]
      for(x in roosalt){
         var createquestli=document.createElement("li")
         createquestli.setAttribute("id", "questlistli")
         createquestli.innerText = roosalt[x].name
         createquestli.className = "dropdown-item"
         var createspanx= document.createElement("span")
         createspanx.className="closequest"
         createspanx.innerHTML="&times;"
         createquestli.appendChild(createspanx)
         a.appendChild(createquestli)
         var closebtns = document.getElementsByClassName("closequest");
         var i
         for(i=0; i<closebtns.length; i++){
            closebtns[i].addEventListener("click", function() {
               if (this.parentElement !== null){
                  pElement = this.parentElement
                  pElement.removeChild(this)
                  data = {
                     "node" : pElement.innerText
                  }
                  csrf=document.getElementById('Debut')
                  fetch('/questroute', {
                     method: 'PUT',
                     body: JSON.stringify(data),
                     headers: {"X-CSRFToken" : csrf.dataset.csrf}
                  })
                  removehighlight()
                  pElement.remove();

               }
            })
         }

      }
   })
}

function highlightancestors(item) {
   if(item.className =="greenbox" && item.parentElement.parentElement.parentElement.children[0].id =="image"){
      item.classList.remove("greenbox")
      item.className = "bluebox"
   }else if(item.className == "greenbox"){
      item.classList.remove("greenbox")
      item.className = "bluebox"
   }else if(item.className =="bluebox" && item.nextElementSibling.children[0].children[0].className =="bluebox"){
      item.classList.remove("bluebox")
      item.classList.add("greenbox")
   }else{
      item.className="greenbox"
   }
   a=item.parentElement.parentElement.parentElement.children[0]
   while(a.id != "image"){
      a.className="bluebox"
      a=a.parentElement.parentElement.parentElement.children[0]
   }
   a=item.nextElementSibling
   if(a !== null){
      b=a.getElementsByTagName("button")
      for(x of b){
         x.classList.remove("bluebox")
         x.classList.remove("greenbox")
      }
   }
}


function getquestnames() {
   fetch('/questmenu', {
      method: 'GET',
   })
   .then(response => response.json())
   .then(result => {
      for (y in result.prapor){
         var praporli = document.createElement("li")
         var prapora = document.createElement("a")
         praporli.setAttribute("id", "praporli" + y)
         prapora.innerHTML = result.prapor[y][1]
         prapora.className= "dropdown-item"
         prapora.setAttribute("href", "/quests/" + result.prapor[y][0])
         document.getElementById("prapordropdown").appendChild(praporli)
         document.getElementById("praporli" + y).appendChild(prapora)
      }
      for (y in result.therapist){
         var therapistli = document.createElement("li")
         var therapista = document.createElement("a")
         therapistli.setAttribute("id", "therapistli" + y)
         therapista.innerHTML = result.therapist[y][1]
         therapista.className= "dropdown-item"
         therapista.setAttribute("href", "/quests/" + result.therapist[y][0])
         document.getElementById("therapistdropdown").appendChild(therapistli)
         document.getElementById("therapistli" + y).appendChild(therapista)
      }
      for (y in result.fence){
         var fenceli = document.createElement("li")
         var fencea = document.createElement("a")
         fenceli.setAttribute("id", "fenceli" + y)
         fencea.innerHTML = result.fence[y][1]
         fencea.className= "dropdown-item"
         fencea.setAttribute("href", "/quests/" + result.fence[y][0])
         document.getElementById("fencedropdown").appendChild(fenceli)
         document.getElementById("fenceli" + y).appendChild(fencea)
      }
      for (y in result.skier){
         var skierli = document.createElement("li")
         var skiera = document.createElement("a")
         skierli.setAttribute("id", "skierli" + y)
         skiera.innerHTML = result.skier[y][1]
         skiera.className= "dropdown-item"
         skiera.setAttribute("href", "/quests/" + result.skier[y][0])
         document.getElementById("skierdropdown").appendChild(skierli)
         document.getElementById("skierli" + y).appendChild(skiera)
      }
      for (y in result.peacekeeper){
         var peacekeeperli = document.createElement("li")
         var peacekeepera = document.createElement("a")
         peacekeeperli.setAttribute("id", "peacekeeperli" + y)
         peacekeepera.innerHTML = result.peacekeeper[y][1]
         peacekeepera.className= "dropdown-item"
         peacekeepera.setAttribute("href", "/quests/" + result.peacekeeper[y][0])
         document.getElementById("peacekeeperdropdown").appendChild(peacekeeperli)
         document.getElementById("peacekeeperli" + y).appendChild(peacekeepera)
      }
      for (y in result.mechanic){
         var mechanicli = document.createElement("li")
         var mechanica = document.createElement("a")
         mechanicli.setAttribute("id", "mechanicli" + y)
         mechanica.innerHTML = result.mechanic[y][1]
         mechanica.className= "dropdown-item"
         mechanica.setAttribute("href", "/quests/" + result.mechanic[y][0])
         document.getElementById("mechanicdropdown").appendChild(mechanicli)
         document.getElementById("mechanicli" + y).appendChild(mechanica)
      }
      for (y in result.ragman){
         var ragmanli = document.createElement("li")
         var ragmana = document.createElement("a")
         ragmanli.setAttribute("id", "ragmanli" + y)
         ragmana.innerHTML = result.ragman[y][1]
         ragmana.className= "dropdown-item"
         ragmana.setAttribute("href", "/quests/" + result.ragman[y][0])
         document.getElementById("ragmandropdown").appendChild(ragmanli)
         document.getElementById("ragmanli" + y).appendChild(ragmana)
      }
      for (y in result.jaeger){
         var jaegerli = document.createElement("li")
         var jaegera = document.createElement("a")
         jaegerli.setAttribute("id", "jaegerli" + y)
         jaegera.innerHTML = result.jaeger[y][1]
         jaegera.className= "dropdown-item"
         jaegera.setAttribute("href", "/quests/" + result.jaeger[y][0])
         document.getElementById("jaegerdropdown").appendChild(jaegerli)
         document.getElementById("jaegerli" + y).appendChild(jaegera)
      }

   })
}

function getquestitems() {
   const table = document.createElement("table")
   table.setAttribute("id", "tablejs")
   const tableheading = document.createElement("th")
   const tableheading2 = document.createElement("th")
   const tablerow = document.createElement("tr")
   tablerow.setAttribute("id", "tablerowjs")
   var x=document.getElementById("quest").value;
   fetch('/itemroute', {
      method: 'POST',
      body: JSON.stringify({
         body: x,
      })
   })
   .then(response => response.json())
   .then(result => {
      // const result2 = JSON.parse(result["message"])
      var y = 0
      var result2 = ""
      document.getElementById("tablejs").remove()
      document.getElementById("table").appendChild(table)
      document.getElementById("tablejs").appendChild(tablerow)
      document.getElementById("tablerowjs").appendChild(tableheading).innerHTML = "Quest"
      document.getElementById("tablerowjs").appendChild(tableheading2).innerHTML = "Number of Items"
      for (y in result){
         tablerowinside = document.createElement("tr")
         tablerowinside.setAttribute("id", "tablerowjs" + y )
         document.getElementById("tablejs").appendChild(tablerowinside)
         var tablecell = document.createElement("td")
         tablecell.innerHTML = "<a href='/quests/" + result[y].slug + "'>" + result[y].quest + "</a>"
         document.getElementById("tablerowjs" + y).appendChild(tablecell)
         var tablecell2 = document.createElement("td")
         tablecell2.innerHTML = result[y].num
         document.getElementById("tablerowjs" + y).appendChild(tablecell2)
      }
   })

}

$(function() {
  // ------------------------------------------------------- //
  // Multi Level dropdowns
  // ------------------------------------------------------ //
  $("ul.dropdown-menu [data-toggle='dropdown']").on("click", function(event) {
    event.preventDefault();
    event.stopPropagation();
    if (!$(this).next().hasClass('show')) {
      $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
    }
    $(this).siblings().toggleClass("show");


    if (!$(this).next().hasClass('show')) {
      $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
    }
    $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
      $('.dropdown-submenu .show').removeClass("show");
    });

  });
});


function getFIRItems(node, csrftoken, clicked_id) {

   function populateList(array1, array2, arraynum){
      a=document.getElementById(array1[0])
      while(a.nextElementSibling !== null){
         for(y of a.nextElementSibling.children){
            array2.push(y.children[0].innerText)
         }
         if (a.nextElementSibling.children.length > 1){
            for(i=1; i<a.nextElementSibling.children.length; i++){
               arrayofparents.push(a.nextElementSibling.children[i].children[0].innerText)
            }
         }
         a=a.nextElementSibling.children[0].children[0]
      }
      return array2
   }

   var childdata = document.getElementById(clicked_id)
   let childarray = []
   let arrayofparents = []
   while(childdata.nextElementSibling !== null){
      for(y of childdata.nextElementSibling.children){
         childarray.push(y.children[0].innerText)
      }
      if (childdata.nextElementSibling.children.length > 1){
         for(i=1; i<childdata.nextElementSibling.children.length; i++){
            arrayofparents.push(childdata.nextElementSibling.children[i].children[0].innerText)
         }
      }
      childdata=childdata.nextElementSibling.children[0].children[0]

   }
   while(arrayofparents.length > 0){
         childarray = populateList(arrayofparents, childarray)
         arrayofparents.shift()
   }


   let data = {
      'node' : node,
      'childnode' : childarray
   }
   fetch('/questroute', {
      method: 'POST',
      body : JSON.stringify(data),
      headers: {"X-CSRFToken" : csrftoken}
   })
   .then(response => response.json())
   .then(result => {
      a=document.getElementById('questsfir')
      a.innerHTML=""
      for(x in result){
         if(document.getElementById("quest" + result[x].quest) == null){
            var questli=document.createElement("h3")
            var itemul=document.createElement("ul")
            var questtext = document.createTextNode(result[x].quest)
            itemul.setAttribute("id", "quest" + result[x].quest)
            a.appendChild(questli)
            questli.appendChild(questtext)
            questli.appendChild(itemul)
         }
         var text = document.createTextNode(result[x].num + "x " + result[x].item)
         var li=document.createElement("li")
         li.appendChild(text)
         document.getElementById("quest" + result[x].quest).appendChild(li)
      }
   })
}
