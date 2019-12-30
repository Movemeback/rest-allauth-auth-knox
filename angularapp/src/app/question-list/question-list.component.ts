import {Component, OnInit} from '@angular/core';

import {QuestionService} from "../question.service";
import {FormBuilder} from "@angular/forms";
import {AuthService} from "../auth.service";



@Component({
  selector: 'app-question-list',
  templateUrl: './question-list.component.html',
})
export class QuestionListComponent implements OnInit {
  questions;
  newForm;

  ngOnInit() {

  }

  constructor(
    private questionService: QuestionService,
    private formBuilder: FormBuilder,
  ) {

    this.newForm = this.formBuilder.group({
      subject: '',
      body: ''
    });
    this.questionService.getItems().subscribe((data) => this.questions = data);
  }

  onSubmit(data) {
    this.questionService.addItem(data).subscribe((responseData) => this.questions.push(data));
    this.newForm.reset();
  }

}
