#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)

# Copyright (c) 2019 CNRS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# AUTHORS
# Hervé BREDIN - http://herve.niderb.fr


class Callback(object):

    def __init__(self):
        super().__init__()

    def load_epoch(self, trainer, epoch):
        pass

    def on_train_start(self, trainer):
        pass

    def on_epoch_start(self, trainer):
        pass

    def on_batch_start(self, trainer, batch):
        return batch

    def on_batch_end(self, trainer, loss):
        pass

    def on_epoch_end(self, trainer):
        pass

    def on_train_end(self, trainer):
        pass


class Callbacks(object):
    def __init__(self, callbacks):
        super().__init__()
        self.callbacks = callbacks

    def load_epoch(self, trainer, epoch):
        for callback in self.callbacks:
            callback.load_epoch(trainer, epoch)

    def on_train_start(self, trainer):
        trainer.on_train_start()
        for callback in self.callbacks:
            callback.on_train_start(trainer)

    def on_epoch_start(self, trainer):
        trainer.epoch_ += 1
        for callback in self.callbacks:
            callback.on_epoch_start(trainer)

    def on_batch_start(self, trainer, batch):
        for callback in self.callbacks:
            batch = callback.on_batch_start(trainer, batch)
        return batch

    def on_batch_end(self, trainer, loss):
        for callback in self.callbacks:
            callback.on_batch_end(trainer, loss)

    def on_epoch_end(self, trainer):
        for callback in self.callbacks:
            callback.on_epoch_end(trainer)

    def on_train_end(self, trainer):
        for callback in self.callbacks:
            callback.on_train_end(trainer)
