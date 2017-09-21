import { BrowserModule } from '@angular/platform-browser';
import {ErrorHandler, isDevMode, NgModule} from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';

import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
import { ListPage } from '../pages/list/list';
import {PersonList} from '../pages/person/personlist'
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import {HttpModule} from "@angular/http";
import {PersonService} from '../common/service/personService'
import {PersonComponent} from "../pages/person/person";
@NgModule({
  declarations: [
    MyApp,
    HomePage,
    ListPage,
    PersonList,
    PersonComponent
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpModule
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    ListPage,
    PersonList,
    PersonComponent

  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    PersonService
  ]
})
export class AppModule {}
