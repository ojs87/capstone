document.addEventListener('DOMContentLoaded', function(){

   getquestnames()
});

function getquestnames() {
   fetch('/questroute', {
      method: 'GET',
   })
   .then(response => response.json())
   .then(result => {
      for (y in result.prapor){
         var praporli = document.createElement("li")
         var prapora = document.createElement("a")
         praporli.setAttribute("id", "praporli" + y)
         prapora.innerHTML = result.prapor[y]
         prapora.className= "dropdown-item"
         prapora.setAttribute("href", "/quests/" + result.prapor[y])
         document.getElementById("prapordropdown").appendChild(praporli)
         document.getElementById("praporli" + y).appendChild(prapora)
      }
      for (y in result.therapist){
         var therapistli = document.createElement("li")
         var therapista = document.createElement("a")
         therapistli.setAttribute("id", "therapistli" + y)
         therapista.innerHTML = result.therapist[y]
         therapista.className= "dropdown-item"
         therapista.setAttribute("href", "/quests/" + result.therapist[y])
         document.getElementById("therapistdropdown").appendChild(therapistli)
         document.getElementById("therapistli" + y).appendChild(therapista)
      }
      for (y in result.fence){
         var fenceli = document.createElement("li")
         var fencea = document.createElement("a")
         fenceli.setAttribute("id", "fenceli" + y)
         fencea.innerHTML = result.fence[y]
         fencea.className= "dropdown-item"
         fencea.setAttribute("href", "/quests/" + result.fence[y])
         document.getElementById("fencedropdown").appendChild(fenceli)
         document.getElementById("fenceli" + y).appendChild(fencea)
      }
      for (y in result.skier){
         var skierli = document.createElement("li")
         var skiera = document.createElement("a")
         skierli.setAttribute("id", "skierli" + y)
         skiera.innerHTML = result.skier[y]
         skiera.className= "dropdown-item"
         skiera.setAttribute("href", "/quests/" + result.skier[y])
         document.getElementById("skierdropdown").appendChild(skierli)
         document.getElementById("skierli" + y).appendChild(skiera)
      }
      for (y in result.peacekeeper){
         var peacekeeperli = document.createElement("li")
         var peacekeepera = document.createElement("a")
         peacekeeperli.setAttribute("id", "peacekeeperli" + y)
         peacekeepera.innerHTML = result.peacekeeper[y]
         peacekeepera.className= "dropdown-item"
         peacekeepera.setAttribute("href", "/quests/" + result.peacekeeper[y])
         document.getElementById("peacekeeperdropdown").appendChild(peacekeeperli)
         document.getElementById("peacekeeperli" + y).appendChild(peacekeepera)
      }
      for (y in result.mechanic){
         var mechanicli = document.createElement("li")
         var mechanica = document.createElement("a")
         mechanicli.setAttribute("id", "mechanicli" + y)
         mechanica.innerHTML = result.mechanic[y]
         mechanica.className= "dropdown-item"
         mechanica.setAttribute("href", "/quests/" + result.mechanic[y])
         document.getElementById("mechanicdropdown").appendChild(mechanicli)
         document.getElementById("mechanicli" + y).appendChild(mechanica)
      }
      for (y in result.ragman){
         var ragmanli = document.createElement("li")
         var ragmana = document.createElement("a")
         ragmanli.setAttribute("id", "ragmanli" + y)
         ragmana.innerHTML = result.ragman[y]
         ragmana.className= "dropdown-item"
         ragmana.setAttribute("href", "/quests/" + result.ragman[y])
         document.getElementById("ragmandropdown").appendChild(ragmanli)
         document.getElementById("ragmanli" + y).appendChild(ragmana)
      }
      for (y in result.jaeger){
         var jaegerli = document.createElement("li")
         var jaegera = document.createElement("a")
         jaegerli.setAttribute("id", "jaegerli" + y)
         jaegera.innerHTML = result.jaeger[y]
         jaegera.className= "dropdown-item"
         jaegera.setAttribute("href", "/quests/" + result.jaeger[y])
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
         tablecell.innerHTML = result[y].quest
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
