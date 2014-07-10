//
//  ViewController.m
//  itunesSockets
//
//  Created by Daniel Klinkert on 7/6/14.
//  Copyright (c) 2014 _danielKlinkert_. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    socket = [[GCDAsyncSocket alloc] initWithDelegate:self delegateQueue:dispatch_get_main_queue()];
    [self.ipTextField setDelegate:self];
    [self.trackTextField setDelegate:self];
    [switchButton setOn:NO];
    slider.minimumValue=0;
    slider.maximumValue=100;
    [slider setValue:100];
    [slider setContinuous:NO];
	// Do any additional setup after loading the view, typically from a nib.
}
- (IBAction)sliderVolume:(id)sender {
    int volum = (int)slider.value;

    self.send = [NSString stringWithFormat:@"%i",volum];
     NSString *sende = [NSString stringWithFormat:@"{\"volume\": %i}", volum];
    
    [socket writeData:[sende dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
    
}
- (IBAction)searchSong:(id)sender {
     self.send =[NSString stringWithFormat:@"{\"trackName\": \"%@\"}", self.trackTextField.text];
    [socket writeData:[self.send dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
    
}
- (IBAction)connect:(id)sender {

    [socket connectToHost:self.ipTextField.text onPort:1024 withTimeout:-1 error:nil];
}
- (IBAction)openItunes:(id)sender {
    if ([switchButton isOn]) {
        self.send =[NSString stringWithFormat:@"{\"open\": \"%@\"}", @"open"];
        [socket writeData:[self.send dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
    }else{
        self.send =[NSString stringWithFormat:@"{\"close\": \"%@\"}", @"close"];
        [socket writeData:[self.send dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
    }
}
- (IBAction)nextTrack:(id)sender {
    self.send =[NSString stringWithFormat:@"{\"nextTrack\": \"%@\"}", @"nextTrack"];
    
    [socket writeData:[self.send dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
}
- (IBAction)trackBack:(id)sender {
    self.send =[NSString stringWithFormat:@"{\"trackBack\": \"%@\"}", @"trackBack"];
    
    [socket writeData:[self.send dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
}
- (IBAction)playAndPause:(id)sender {
    self.send =[NSString stringWithFormat:@"{\"play\": \"%@\"}", @"play"];
    
    [socket writeData:[self.send dataUsingEncoding:NSUTF8StringEncoding] withTimeout:-1 tag:0];
}

- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event{
    [self.ipTextField resignFirstResponder];
    [self.trackTextField resignFirstResponder];
}
- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
