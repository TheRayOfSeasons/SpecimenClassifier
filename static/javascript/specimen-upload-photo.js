const directions = ['north', 'east', 'west', 'south'];

const buildImageId = (direction, number) =>
{
    return `${direction}-${number.toString()}`;
}

const buildCollectionSelector = (direction) =>
{
    return `#${direction}Images`;
}

const buildImageButtonSelector = (direction, number) =>
{
    return `${direction}ImageButton-${number}`;
}

const buildImageButtonName = (direction, number) =>
{
    return `${direction}Image-${number}`
}

const generateNewImageButton = (direction, number) =>
{
    let i = number + 1;
    let name = buildImageButtonName(direction, i);
    let selector = buildImageButtonSelector(direction, i);
    return `<input type="file" name="${name}" value="fileupload" id="${selector}" onChange="displayUploaded(this, '${direction}', ${i})">`
}

const insertImage = (direction, number) =>
{
    const imageCollection = buildCollectionSelector(direction);
    const generateImageElement = new Promise((resolve) =>
    {
        let i = number;
        let imageID = buildImageId(direction, i);

        resolve(
            {
                template: `<img id='${imageID}' src="#">`,
                id: imageID,
            }
        );
    });

    return generateImageElement.then((newImage) => {
        $(imageCollection).prepend(newImage.template);
        $(imageCollection).append(generateNewImageButton(direction, number))
        return '#' + newImage.id;
    });
}

const displayUploaded = (input, direction, number) =>
{
    insertImage(direction, number).then((id) => {
        if (input.files && input.files[0])
        {
            var reader = new FileReader();

            reader.onload = (e) =>
            {
                $(id)
                    .attr('src', e.target.result)
                    .width(150)
                    .height(200);
            };

            reader.readAsDataURL(input.files[0]);
        }
    });
}
