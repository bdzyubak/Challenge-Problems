def train_model(model, loader_train, model_save_file=None, loader_val=None, epochs=3, device='cuda:0'):
    model.to(device)
    optim = AdamW(model.parameters(), lr=5e-5)
    for epoch in range(1, epochs):
        model.train()
        epoch_loss = 0.0
        for (b_ix, batch) in enumerate(loader_train):
            optim.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs[0]
            epoch_loss += loss.item()  # accumulate batch loss
            loss.backward()
            optim.step()

        print(f"Epoch {epoch} loss: {epoch_loss}")

        if loader_val is not None:
            model.eval()
            preds = predict_tokenized_classification(model, loader_val, device='cuda:0')
            acc_epoch = accuracy_score(preds, loader_val.dataset.labels_class)
            print(f"Epoch {epoch} val accuracy: {acc_epoch}")

        if model_save_file is not None and epoch % 10 == 0:
            torch.save(model.state_dict(), model_save_file.parent / (model_save_file.stem + f'_epoch{epoch}.pth'))

    print("Training done ")
    model.eval()
