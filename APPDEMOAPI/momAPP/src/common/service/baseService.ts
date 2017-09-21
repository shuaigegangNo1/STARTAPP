/**
 * Created by simonsu on 17-7-20.
 */
import {Observable} from "rxjs/Rx";
import {AlertController} from "ionic-angular";
export abstract class BaseService{
  constructor(public alertCtrl: AlertController){
  }
  protected handleError(error){
    let errorMessage =error.json().message;
    if(error.json().error){
      errorMessage += ":" + error.json().error;
    }
    // let alert = this.alertCtrl.create(
    //   {
    //     title: '网络异常',
    //     subTitle: '正在抢救中...',
    //     buttons: ['确认']
    //   });
    // alert.present();
    switch (error.status){
      case 401:
            return Observable.throw("invalid token");
      default:
            return Observable.throw(errorMessage);
    }
  }
}
