let sequenceForm = document.querySelectorAll("#sequence-form");
let addButton = document.querySelector("#add-form");
let totalForms = document.querySelector("#id_sequences-TOTAL_FORMS");
let container = document.querySelector("#form-container");
let formNum = sequenceForm.length-1;

addButton.addEventListener('click', addForm);

function addForm(e) {
e.preventDefault();

let newForm = sequenceForm[0].cloneNode(true);    //Clone the sequence form

let pattern = RegExp('sequences-(\\d)+-','g');    //Regex to find all instances of the form number
formNum++;                                        //Increment the form number

newForm.innerHTML = newForm.innerHTML.replace(pattern, `sequences-${formNum}-`);

container.insertBefore(newForm, addButton); //Insert the new form at the end of the list of forms
totalForms.setAttribute('value', `${formNum+1}`); //Increment the number of total forms in the management form
};


let deleteButtons = document.querySelector(".delete-form");

deleteButtons.addEventListener('click', deleteForm);

function deleteForm(e) {
e.preventDefault();

console.log(e);
//let pattern = RegExp('sequences-(\\d)+-','g');    //Regex to find all instances of the form number
//formNum++;                                        //Increment the form number
//
//newForm.innerHTML = newForm.innerHTML.replace(pattern, `sequences-${formNum}-`);
//
//container.insertBefore(newForm, addButton); //Insert the new form at the end of the list of forms
//totalForms.setAttribute('value', `${formNum+1}`); //Increment the number of total forms in the management form
}