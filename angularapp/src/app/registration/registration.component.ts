import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import {QuestionService} from "../question.service";
import {FormBuilder} from "@angular/forms";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
})
export class RegistrationComponent implements OnInit {
  registrationForm;
  result;
  constructor(
    private router: Router,
    private formBuilder: FormBuilder,
    private authService: AuthService
  ) {

    this.registrationForm = this.formBuilder.group({
      first_name: '',
      last_name: '',
      username: '',
      password: ''
    });

  }

  ngOnInit() {
  }

  onSubmit(data) {
    this.authService.login(data['first_name'], data['last_name']).subscribe( (response) => {
      this.result = response; this.router.navigate(['/']);
    })
  }

}
