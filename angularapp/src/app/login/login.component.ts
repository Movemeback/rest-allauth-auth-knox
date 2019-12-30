import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import {FormBuilder} from "@angular/forms";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
})
export class LoginComponent implements OnInit {
  loginForm;
  result;
  constructor(
    private route: ActivatedRoute,
    private formBuilder: FormBuilder,
    private authService: AuthService
  ) {

    this.loginForm = this.formBuilder.group({
      username: '',
      password: ''
    });

  }

  ngOnInit() {

  }

  onSubmit(data) {
    console.log(data);
    this.authService.login(data['username'], data['password']).subscribe( (response) => this.result = response );
  }

}
