//
//  ViewController.h
//  itunesSockets
//
//  Created by Daniel Klinkert on 7/6/14.
//  Copyright (c) 2014 _danielKlinkert_. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GCDAsyncSocket.h"

@interface ViewController : UIViewController<UITextFieldDelegate,GCDAsyncSocketDelegate>{
    
    __weak IBOutlet UISlider *slider;
    __weak IBOutlet UISwitch *switchButton;
    GCDAsyncSocket *socket;
}
@property (weak, nonatomic) IBOutlet UITextField *ipTextField;
@property (weak, nonatomic) IBOutlet UITextField *trackTextField;
@property (weak, nonatomic) IBOutlet UIButton *playPauseButton;

@property(copy,nonatomic)NSString * send;
@end
