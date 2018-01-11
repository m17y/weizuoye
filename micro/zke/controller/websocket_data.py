# -*- coding:utf-8 -*-
import json
from base import BaseHandler,BaseSocketHandler
from logic.access import *



# @url(r"/websocket/real_time_monitor")
class WebsocketRealTimeMonitorHandler(BaseSocketHandler):
    """监控面板实时推送"""
    def on_message(self, msg):
        msg = json.loads(msg)
        if msg.get('cmd', '') == 'async_client':
            code_name = msg.get('code_name', '')
            fj_no = msg.get('fj_no')
            _type = msg.get('type','')
            opt = msg.get('opt','')
            if not code_name:
                return
            value = code_name + '_' +fj_no
            try:
                if 'add' == opt :
                    BaseSocketHandler.waiters_filter[self].add(value)
                    _data =MongoIns().m_find_one('newest_data',_id=fj_no,dbname=code_name)
                    for k,v in _data.items():
                        if k not in WT_REAKL_TILE_MAP.values():
                            _data.pop(k)
                    self.write_message(_data)
                if _type == 'zd':
                    value = value+'_'+'zd'
                    print value
                    BaseSocketHandler.waiters_filter[self].add(value)
            except Exception as e:
                traceback.print_exc()
        else:
            code_name = msg.get('code_name', '')
            fj_no = msg.get('fj_no')
            _type = msg.get('type','')
            value=None
            value = code_name + '_' + fj_no
            result={}
            if not _type:
                alldata = code_name + '_all'
                for k,v in msg.items():
                    if k not in WT_REAKL_TILE_MAP.values():
                        msg.pop(k)
                        msg['fj_num'] = fj_no

                _id =msg['fj_num'] + "_" + time.strftime("%Y-%m-%d", time.localtime(msg.get('ts')))
                Energy =  MongoIns().m_find_one("data_d", dbname = code_name, _id = _id, fields = {'Energy': 1}).get('Energy')
                if Energy:
                    msg['Energy'] = round(Energy, 2)
                if alldata in BaseSocketHandler.waiters_filter[self]: 
                    self.write_message(msg)
                elif value in BaseSocketHandler.waiters_filter[self]: 
                    self.write_message(msg)
            else:
                value = value+'_'+'zd'
                if value in BaseSocketHandler.waiters_filter[self]: 
                    self.write_message(msg)

# var updater = {
#   socket: null,
#   start: function() {
#     var url = "ws://" + location.host + "/websocket/real_time_monitor";
#     updater.socket = new WebSocket(url);
#     updater.socket.onopen = function(event) {
#       console.log('open-websocket:', event);
#       updater.socket.send(JSON.stringify({
#         'cmd': 'async_client',
#         'code_name': 'wf_TieLing',
#         'cmd': 'async_client',
#         'fj_no': 'fj_31',
#         'type': 'zd',
#         'opt':'add'
#       }))
#     };
#     updater.socket.onmessage = function(event) {
#       console.log('message-websocket:', event);
#     };
#     updater.socket.onclose = function(event) {
#       window.setTimeout(updater.start, 5000);
#       console.log('close:', event);
#     };
#     updater.socket.onerror = function(event) {
#       console.log('error:', event);
#     };
#   }
# };

# $("#real_time_monitor").click(function() {
#   updater.start();
# })