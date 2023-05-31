function imprimirPDF() {
    window.jsPDF = window.jspdf.jsPDF;
    let doc = new jsPDF();

    let imprer = document.getElementById("carnet");
  
    var elementHTML = document.body;

    doc.html(imprer, {
      callback: function (doc) {
        doc.save("carnet-seguro.pdf");
      },
      x: 15,
      y: 15,
      width: 170, //target width in the PDF document
      windowWidth: 650, //window width in CSS pixels
    });

  }