/****************************************************************************
** Meta object code from reading C++ file 'framecapture.h'
**
** Created: Sun Aug 5 18:57:30 2012
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "framecapture.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'framecapture.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_FrameCapture[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      14,   13,   13,   13, 0x05,

 // slots: signature, parameters, type, tag, flags
      33,   25,   13,   13, 0x08,
      55,   52,   13,   13, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_FrameCapture[] = {
    "FrameCapture\0\0finished()\0percent\0"
    "printProgress(int)\0ok\0saveResult(bool)\0"
};

void FrameCapture::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        FrameCapture *_t = static_cast<FrameCapture *>(_o);
        switch (_id) {
        case 0: _t->finished(); break;
        case 1: _t->printProgress((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->saveResult((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData FrameCapture::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject FrameCapture::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_FrameCapture,
      qt_meta_data_FrameCapture, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &FrameCapture::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *FrameCapture::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *FrameCapture::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_FrameCapture))
        return static_cast<void*>(const_cast< FrameCapture*>(this));
    return QObject::qt_metacast(_clname);
}

int FrameCapture::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void FrameCapture::finished()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
