config = {
    'version': 'v1',
    'config': {
        'visState': {
            'filters': [{
                'dataId': ['unnamed'],
                'id': 'kpyhofh2c',
                'name': ['richter'],
                'type': 'range',
                'value': [3, 7.2],
                'enlarged': False,
                'plotType': 'histogram',
                'animationWindow': 'free',
                'yAxis': None,
                'speed': 1
            }, {
                'dataId': ['unnamed'],
                'id': 'ea0fepd6',
                'name': ['country'],
                'type': 'multiSelect',
                'value': ['turkey', 'cyprus_turkish'],
                'enlarged': False,
                'plotType': 'histogram',
                'animationWindow': 'free',
                'yAxis': None,
                'speed': 1
            }],
            'layers': [{
                'id': 'wjii32k',
                'type': 'heatmap',
                'config': {
                    'dataId':
                    'unnamed',
                    'label':
                    'new layer',
                    'color': [248, 149, 112],
                    'highlightColor': [252, 242, 26, 255],
                    'columns': {
                        'lat': 'lat',
                        'lng': 'long'
                    },
                    'isVisible':
                    True,
                    'visConfig': {
                        'opacity': 0.8,
                        'colorRange': {
                            'name':
                            'Global Warming',
                            'type':
                            'sequential',
                            'category':
                            'Uber',
                            'colors': [
                                '#5A1846', '#900C3F', '#C70039', '#E3611C',
                                '#F1920E', '#FFC300'
                            ]
                        },
                        'radius': 4
                    },
                    'hidden':
                    False,
                    'textLabel': [{
                        'field': None,
                        'color': [255, 255, 255],
                        'size': 18,
                        'offset': [0, 0],
                        'anchor': 'start',
                        'alignment': 'center'
                    }]
                },
                'visualChannels': {
                    'weightField': None,
                    'weightScale': 'linear'
                }
            }],
            'interactionConfig': {
                'tooltip': {
                    'fieldsToShow': {
                        'unnamed': [{
                            'name': 'date',
                            'format': None
                        }, {
                            'name': 'time',
                            'format': None
                        }, {
                            'name': 'country',
                            'format': None
                        }, {
                            'name': 'richter',
                            'format': None
                        }]
                    },
                    'compareMode': False,
                    'compareType': 'absolute',
                    'enabled': True
                },
                'brush': {
                    'size': 0.5,
                    'enabled': False
                },
                'geocoder': {
                    'enabled': False
                },
                'coordinate': {
                    'enabled': False
                }
            },
            'layerBlending':
            'normal',
            'splitMaps': [],
            'animationConfig': {
                'currentTime': None,
                'speed': 1
            }
        },
        'mapState': {
            'bearing': 0,
            'dragRotate': False,
            'latitude': 38.725370895029585,
            'longitude': 35.277099610085116,
            'pitch': 0,
            'zoom': 4.9936178358907695,
            'isSplit': False
        },
        'mapStyle': {
            'styleType':
            'dark',
            'topLayerGroups': {},
            'visibleLayerGroups': {
                'label': True,
                'road': True,
                'border': False,
                'building': True,
                'water': True,
                'land': True,
                '3d building': False
            },
            'threeDBuildingColor':
            [9.665468314072013, 17.18305478057247, 31.1442867897876],
            'mapStyles': {}
        }
    }
}